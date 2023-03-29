from user import User
from post import Post

app_user_one = User("sogogo@gmail.com", "Samosanction", "pwd1", "Developer")
app_user_one.get_user_info()

app_user_two = User("dorixy@gmail.com", "Dorixy", "pwd1", "Healthcare Assistant")
app_user_two.get_user_info()

new_post = Post(f"I am the best guy here", app_user_one.name)
new_post.get_post_info()
