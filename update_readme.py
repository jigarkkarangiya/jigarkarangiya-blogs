import requests

# Function to fetch blog posts from WordPress site
def fetch_blog_posts():
    url = 'https://jigarkarangiya.com/wp-json/wp/v2/posts'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error fetching blog posts: {response.status_code}')
        return None

# Function to update README.md file with blog post details
def update_readme(blog_posts):
    if blog_posts:
        table_content = "| Serial No | Blog Name | Blog URL |\n| --------- | --------- | -------- |\n"
        for index, post in enumerate(blog_posts, start=1):
            title = post['title']['rendered']
            post_url = post['link']
            table_content += f"| {index} | {title} | {post_url} |\n"
        
        with open('README.md', 'w') as readme_file:
            readme_file.write(table_content)
        print('README.md updated successfully.')
    else:
        print('No blog posts to update.')

if __name__ == '__main__':
    blog_posts = fetch_blog_posts()
    update_readme(blog_posts)
