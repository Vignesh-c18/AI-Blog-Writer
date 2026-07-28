import json
import boto3
from pathlib import Path
from typing import Optional, List, Dict, Any
from botocore.exceptions import ClientError

from blogboard.config.settings import app_settings


class R2StorageService:
    """
    Storage service.

    - If R2 is configured, uses Cloudflare R2.
    - Otherwise, automatically uses local files under output/.
    """

    def __init__(self):
        self.bucket_name = app_settings.r2.BUCKET_NAME.strip(' ="\'')

        if not app_settings.r2.ACCOUNT_ID:
            self.client = None
            self.bucket_name = None
            return

        self.client = boto3.client(
            service_name="s3",
            endpoint_url=f"https://{app_settings.r2.ACCOUNT_ID}.r2.cloudflarestorage.com",
            aws_access_key_id=app_settings.r2.ACCESS_KEY_ID,
            aws_secret_access_key=app_settings.r2.SECRET_ACCESS_KEY,
            region_name="auto",
        )

    # ------------------------------------------------------------------
    # RAW FILES
    # ------------------------------------------------------------------

    def get_object(self, key: str) -> Optional[str]:
        """Read a text file from local storage or R2."""

        # ---------- Local Mode ----------
        if self.client is None:
            local_path = Path("output") / key

            if not local_path.exists():
                return None

            try:
                with open(local_path, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                print(f"[ERROR] Failed reading {local_path}: {e}")
                return None

        # ---------- R2 Mode ----------
        try:
            response = self.client.get_object(
                Bucket=self.bucket_name,
                Key=key,
            )
            return response["Body"].read().decode("utf-8")

        except ClientError as e:
            if e.response["Error"]["Code"] == "NoSuchKey":
                return None

            print(f"[ERROR] R2 error in get_object ({key}): {e}")
            return None

        except Exception as e:
            print(f"[ERROR] Unexpected error fetching {key}: {e}")
            return None

    def put_object(
        self,
        key: str,
        data: str,
        content_type: str = "text/plain",
    ) -> bool:
        """Save a file locally or upload to R2."""

        # ---------- Local Mode ----------
        if self.client is None:
            local_path = Path("output") / key
            local_path.parent.mkdir(parents=True, exist_ok=True)

            with open(local_path, "w", encoding="utf-8") as f:
                f.write(data)

            print(f"  ✅ Saved locally: {local_path}")
            return True

        # ---------- R2 Mode ----------
        try:
            self.client.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=data.encode("utf-8"),
                ContentType=content_type,
            )

            print(f"  ✅ Uploaded to R2: {self.bucket_name}/{key}")
            return True

        except ClientError as e:
            print(f"[ERROR] Failed uploading {key}: {e}")
            return False

    # ------------------------------------------------------------------
    # JSON HELPERS
    # ------------------------------------------------------------------

    def get_json(self, key: str) -> List[Dict[str, Any]]:
        data = self.get_object(key)

        if not data:
            return []

        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return []

    def get_articles_json(self, domain: str) -> List[Dict[str, Any]]:
        return self.get_json(f"blogs/{domain}/articles.json")

    def save_articles_json(
        self,
        domain: str,
        articles: List[Dict[str, Any]],
    ) -> bool:
        return self.put_object(
            f"blogs/{domain}/articles.json",
            json.dumps(articles, indent=2, ensure_ascii=False),
            content_type="application/json",
        )

    # ------------------------------------------------------------------
    # HISTORY
    # ------------------------------------------------------------------

    def get_recent_history(
        self,
        domain: str,
        limit: int = 3,
    ) -> List[Dict[str, Any]]:
        articles = self.get_articles_json(domain)

        articles = sorted(
            articles,
            key=lambda x: x.get("date", ""),
            reverse=True,
        )

        recent = articles[:limit]

        return [
            {
                "title": a.get("title"),
                "topic": a.get("topic"),
                "subtopics": a.get("subtopics", ""),
            }
            for a in recent
        ]

    def get_all_domains_last_updated(self) -> Dict[str, str]:
        latest = {}

        for domain in app_settings.tags.model_dump().keys():
            articles = self.get_articles_json(domain)

            if not articles:
                latest[domain] = "Never"
                continue

            articles = sorted(
                articles,
                key=lambda x: x.get("date", ""),
                reverse=True,
            )

            latest[domain] = articles[0].get("date", "Unknown")

        return latest