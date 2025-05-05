# from langchain_community.utilities import SerpAPIWrapper
# class CustomSerpAPIWrapper(SerpAPIWrapper):
#     def __init__(self):
#         super(CustomSerpAPIWrapper, self).__init__()
#
#     @staticmethod
#     def _process_response(res: dict) -> str:
#         """Process response from SerpAPI."""
#         if "error" in res.keys():
#             raise ValueError(f"Got error from SerpAPI: {res['error']}")
#         if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
#             toret = res["answer_box"]["answer"]
#         elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
#             toret = res["answer_box"]["snippet"]
#         elif (
#             "answer_box" in res.keys()
#             and "snippet_highlighted_words" in res["answer_box"].keys()
#         ):
#             toret = res["answer_box"]["snippet_highlighted_words"][0]
#         elif (
#             "sports_results" in res.keys()
#             and "game_spotlight" in res["sports_results"].keys()
#         ):
#             toret = res["sports_results"]["game_spotlight"]
#         elif (
#             "knowledge_graph" in res.keys()
#             and "description" in res["knowledge_graph"].keys()
#         ):
#             toret = res["knowledge_graph"]["description"]
#         elif "snippet" in res["organic_results"][0].keys():
#             toret = res["organic_results"][0]["link"]
#
#         else:
#             toret = "No good search result found"
#         return toret
#
#
# def get_profile_url(name: str):
#     """Searches for Linkedin or twitter Profile Page."""
#     search = CustomSerpAPIWrapper()
#     res = search.run(f"{name}")
#     return res

#Tool that queries the Tavily Search API and gets back json.
# pip install -U langchain-community tavily-python  
# export TAVILY_API_KEY="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"

from langchain_community.tools import TavilySearchResults

def get_profile_url_tavily(name: str) -> str:
    """Searches for LinkedIn Profile URL using Tavily."""

    search = TavilySearchResults(
            max_results=5,
            include_answer=True,
            include_raw_content=True,
            include_images=True,
            # search_depth="advanced",
            # include_domains = []
            # exclude_domains = []
        )

    results = search.run(f"{name}")

    # Iterate through results and look for a LinkedIn URL
    for item in results:
        url = item.get("url", "")
        if "linkedin.com" in url.lower():
            return url

    return ""  # Return empty string if no LinkedIn URL found