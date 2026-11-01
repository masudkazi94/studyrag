from youtubesearchpython import VideosSearch

def get_yt_video_link(query):
    try:
        video_search = VideosSearch(query=query, limit=3)
        result = video_search.result()
        
        video_titles = [video['title'] for video in result['result']]
        video_links = [video['link'] for video in result['result']]
        
        return video_titles, video_links
        
    except Exception as e:
        print(f"YouTube search failed: {e}")
        return ["Video search unavailable"], ["#"]