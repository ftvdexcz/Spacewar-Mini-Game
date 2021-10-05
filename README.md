<h1> Spacewar-Mini-Game </h1>
<i>Bài tập lớn môn Python<i>
  
<h2>Cài đặt</h2> 
  
  `pip install pygame`

<h2>Cấu trúc file</h2>
<ul>
  <li>Các file lưu các đối tượng trong game
    <ul>
    <li>Ship.py: class cha</li>
    <li>Enemy.py: đối tượng tàu địch kế thừa từ Ship</li>
    <li>Player.py: đối tượng tàu người chơi kế thừa từ Ship</li>
    <li>Laser.py: đối tượng đạn bắn ra từ tàu</li>
    </ul>
  </li>
  <li>config.py: file cấu hình các biến, hình ảnh, font...</li>
  <li>main.py: xử lí chương trình</py>
  <li>run_game.py: chạy game, menu</li>
  <li>Thư mục assets lưu hình ảnh trong game</li>
</ul>
<h2>Chạy chương trình và thay đổi cấu hình</h2>
<b>Chạy game: chạy file run_game.py</b><br>
<b>Cấu hình: Thay đổi trong file config.py<b><br>
<hr>
<p>Thay đổi cách hoạt động của tàu địch trong file main.py</p>

 
1. Vị trí khởi tạo ngẫu nhiên tàu địch 
  
```
enemy = Enemy(random.randrange(50, WIDTH-100),random.randrange(-1500, -100), random.choice(['red', 'green', 'blue']))
enemies.append(enemy)
```
<br>
2. Xác suất bắn của tàu địch
  
```
if random.randrange(0, 3*FPS) == 1:
    enemy.shoot()
```

  
