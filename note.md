## rewriting git history (removing sensitive data)
https://www.youtube.com/watch?v=Bo-8EfDpKxA&ab_channel=DanGitschooldude

## List Comprehension
`new_list = [new_item for item in list if test]`

## Dictionary Comprehension
`new_dict = {new_key:new_value for (key, value) in dict.item() if test}`

Example of dictionary list comprehension from pandas's csv file

`data = [{"Word": row[1], "Definition": row[3]} for _, row in df.iterrows()]`

## Web Scrapping Okay?
if you have an url add "/robots.txt" will tell you what endpoints they allow/disallow

example: https://news.ycombinator.com/robots.txt

User-Agent: *
Disallow: /x?
Disallow: /r?
Disallow: /vote?
Disallow: /reply?
Disallow: /submitted?
Disallow: /submitlink?
Disallow: /threads?
Crawl-delay: 30