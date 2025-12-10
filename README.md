# 📘 README — Thuật toán Graph, Tree, Spanning Tree và MST trong Python

## 🧩 1. Giới thiệu
Project này triển khai các thuật toán cơ bản trong lý thuyết đồ thị sử dụng Python, bao gồm:

- Biểu diễn đồ thị vô hướng có trọng số (Adjacency List)
- Kiểm tra một đồ thị có phải là **Tree**
- Sinh **Spanning Tree** bằng DFS
- Tìm **Minimum Spanning Tree (MST)** bằng thuật toán **Prim**

Mã nguồn được chia thành 3 file chính:

```
graph.py        → Định nghĩa cấu trúc đồ thị
tree_utils.py   → Hàm kiểm tra Tree, Spanning Tree, MST
run.py          → File chạy chương trình
```

## 🧱 2. Mô hình biểu diễn đồ thị

Đồ thị được lưu bằng **danh sách kề (adjacency list)**:

```
A: [(B,9), (D,6), (H,8)]
B: [(A,9), (D,19), (E,7)]
...
```

Ưu điểm:
- Tiết kiệm bộ nhớ hơn ma trận kề
- Duyệt nhanh bằng BFS/DFS
- Phù hợp cho đồ thị thưa (sparse graph)

Ngoài ra, hàm `edges` tạo ra danh sách cạnh không trùng lặp:

```
[(A, B, 9), (A, D, 6), (B, D, 19), ...]
```

## 🌳 3. Thuật toán kiểm tra Tree (`is_tree`)

Một đồ thị vô hướng là **Tree** nếu:

1. **Không có chu trình**  
2. **Liên thông**  
3. **Số cạnh = số đỉnh − 1**

Thuật toán sử dụng **DFS** để phát hiện chu trình:

### 🔎 Ý tưởng:
- Duyệt từ 1 đỉnh bất kỳ bằng DFS.
- Nếu gặp lại một đỉnh đã thăm mà **không phải cha** → có chu trình → không phải Tree.
- Sau DFS nếu số đỉnh đã thăm ≠ tổng số đỉnh → không liên thông → không phải Tree.
- Cuối cùng kiểm tra số cạnh: `|E| = |V| - 1`.

Nhờ kết hợp cả ba điều kiện → đảm bảo kết quả chính xác.

## 🌿 4. Sinh Spanning Tree bằng DFS (`spanning_tree_dfs`)

Spanning Tree là **cây bao trùm** toàn bộ đỉnh của đồ thị.

### 🔧 Ý tưởng:
- Chọn đỉnh bắt đầu `start`.
- Duyệt DFS.  
- Mỗi khi đi từ u → v (v chưa thăm), cạnh đó được **lấy vào Spanning Tree**.
- Sau khi DFS xong → ta có một Spanning Tree hợp lệ.

Lưu ý: nếu đồ thị không liên thông, cây chỉ bao trùm được thành phần chứa `start`.

## 🔥 5. Thuật toán Prim (Minimum Spanning Tree – MST)

Prim sinh ra MST bằng cách luôn chọn **cạnh nhẹ nhất** nối từ tập đỉnh đã chọn đến đỉnh chưa chọn.

### 📌 Ý tưởng:
1. Bắt đầu từ một đỉnh bất kỳ.
2. Đưa các cạnh kề vào **min-heap (priority queue)**.
3. Mỗi lần lấy ra cạnh có trọng số nhỏ nhất.
4. Nếu đỉnh cuối chưa được chọn → thêm vào MST.
5. Tiếp tục cho đến khi chọn đủ `|V| - 1` cạnh.

## 🧪 6. File run.py — Chạy thử ví dụ

Chương trình tạo đồ thị mẫu, sau đó kiểm tra:

- Danh sách đỉnh  
- Danh sách cạnh  
- Đồ thị có phải Tree hay không  
- Spanning Tree bằng DFS  
- MST bằng Prim  

## 📂 7. Cấu trúc project

```
project/
│
├── graph.py
├── tree_utils.py
├── run.py
└── README.md
```

## ▶️ 8. Cách chạy chương trình

```
python run.py
```

## 📌 9. Kết luận

Project cung cấp:

- Mô hình đồ thị rõ ràng và dễ mở rộng  
- Kiểm tra Tree bằng DFS + điều kiện số cạnh  
- Sinh Spanning Tree bằng DFS  
- Tìm MST bằng Prim  

Có thể mở rộng thêm:
- Chu trình (cycle detection)
- BFS/DFS tổng quát
- Đồ thị có hướng
- Kruskal MST
- Topological Sort

🎉 **README đã sẵn sàng!**
