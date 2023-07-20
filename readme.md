### Cài đặt thư viện
`pip install pytube==15.0.0`


* Khi chạy chương trình bị lỗi: pytube.exceptions.RegexMatchError: get_transform_object: could not find match for var for={(.*?)};

Bước 1: mở file cipher.py của thư viện pytube (file bị lỗi).
(Ví dụ đường dẫn: .venv/lib/python3.10/site-packages/pytube/cipher.py)

Bước 2: Tìm tới hàm get_transform_object(js: str, var: str) và thay thế bằng hàm bên dưới
```
def get_transform_object(js: str, var: str) -> List[str]:
    pattern = r"var %s={(.*?)};" % re.escape(var)
    logger.debug("getting transform object")
    regex = re.compile(pattern, flags=re.DOTALL)
    transform_match = regex.search(js)
    
    if not transform_match:
        # i commented out the line raising the error
        # raise RegexMatchError(caller="get_transform_object", pattern=pattern)
        logger.error(f"No match found for pattern: {pattern}")
        return []  # Return an empty list if no match is found

    return transform_match.group(1).replace("\n", " ").split(", ")
```

Sau đó lưu file và chạy lại chương trình

Link debug: https://stackoverflow.com/questions/76704097/pytube-exceptions-regexmatcherror-get-transform-object-could-not-find-match-fo?fbclid=IwAR00r18hwgwoyBs6vlGnt6a4Q_ndRY3pZGXveb_Oar2OFdQB8qFcGtlOx94