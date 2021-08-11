const loadButtonBlock = document.getElementById("load-button-block");
const loadButton = document.getElementById("load-button");
var posts_count = Number({{posts_count}});
var posts_loaded = 5;
var postBlock = document.getElementById("post-block");
var firstPost = document.querySelectorAll("div.post")[0];

function buildPostPreview(post_id, title, username, timestamp) {
  var html = `<div class="post" id="post-${post_id}">
                <div class="post card columns is-mobile" style="margin:0 0 10px 0" >
                  <div class="column is-paddingless">
                    <a href="/post/${post_id}" onmouseover="this.style.opacity='0.7';"
                      onmouseout="this.style.opacity='1';" class="hero">
                      <div class="hero-body level" style="padding:30px">
                        <div class="container">
                          <h1 class="title is-3 level-left" name="title">${title}</h1>
                          <h1 class="subtitle level-left" name="by">by ${username}</h1>
                        </div>
                        <div class="container level-right">
                          <h1 class="subtitle level-right">${timestamp}</h1>
                        </div>
                      </div>
                    </a>
                  </div>
                </div>
              </div>`;
  return html;
}

function loadPosts() {
  fetch(window.origin+"/get_posts?"+ new URLSearchParams({
    user_id: {{user.id}},
    offset: posts_loaded,
    count: 5
  }),
  {
    method: "GET",
    headers: {
    "Content-Type": "application/json"
    }
  })
  .then(function(responce) {
    responce.json().then((data) => {
      posts = data.posts;
      posts_loaded += posts.length;
      posts.forEach((post) => {
        var newPost = buildPostPreview(post.id, post.title,
          post.author_username, post.timestamp);
        postBlock.insertAdjacentHTML("beforeend", newPost);
      });

      if (posts_count === posts_loaded) {
        loadButton.remove();
      }

    });
  })
  .catch(function(error) {
    console.log("Fetch error: "+ error);
  });
}
document.addEventListener('DOMContentLoaded', () => {
  if (loadButton) {
    loadButton.addEventListener("click", () => {
      loadPosts();
    })
  }
});
