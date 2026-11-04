import logging

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import tool

from app.config.settings import settings

logger = logging.getLogger(__name__)


def create_web_search_tool():
    search = GoogleSerperAPIWrapper(serper_api_key=settings.SERPER_API_KEY)

    @tool
    def web_search(query: str) -> str:
        """search the web for present updated information.

        use this tool whenever user asks about recent events, changes,  latest updated or anything that required web search
        """
        logger.info("Web search started: %s", query)


        try:
            results = search.run(query)
            logger.info("Web search completed successfully.")
            return results

        except Exception:
            logger.exception("Web search failed.")
            raise

    return web_search
