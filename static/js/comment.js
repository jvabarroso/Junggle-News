document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.comments-list .comment-item').forEach(item => {

    const ts = document.createElement('div');
    ts.className = 'comment-timestamp';
    ts.textContent = new Date().toLocaleString();
    item.append(ts);

    const btn = document.createElement('button');
    btn.className = 'like-btn';
    btn.innerHTML = '👍 <span class="count">0</span>';

    btn.addEventListener('click', () => {
      const count = btn.querySelector('.count');
      count.textContent = parseInt(count.textContent) + 1;
    });

    item.append(btn);
  });
});
