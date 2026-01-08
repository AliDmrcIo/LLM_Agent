# tools.py
from ddgs import DDGS

def search_internet(query: str, max_results: int = 3):
    """
    3 Sonuç getirir ve metinleri birleştirir.
    Dönüş: {'summary': '...uzun metin...', 'url': 'ilk_link'}
    """
    clean_query = query.strip()
    filters = " -site:zhihu.com -site:baidu.com -site:bilibili.com"
    final_query = clean_query + filters
    
    print(f"\nSearching....: '{clean_query}'...")
    
    try:
        with DDGS(timeout=30) as ddgs:
            results = list(ddgs.text(
                final_query,
                region='us-en',
                safesearch='moderate',
                max_results=max_results,
                backend='html'
            ))
            
            if not results:
                return None
            
            # 3 sonucun metnini birleştirip tek bir "Bilgi Yığını" yapıyoruz
            combined_summary = ""
            for i, res in enumerate(results, 1):
                combined_summary += f"[Source {i}]: {res.get('body', '')}\n"
            
            # Link olarak en güvenilir görünen ilk linki alalım
            first_url = results[0].get('href', '')
            
            return {
                "summary": combined_summary,
                "url": first_url
            }

    except Exception as e:
        print(f"Hata: {e}")
        return None