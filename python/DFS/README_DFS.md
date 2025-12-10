
# 🌳 Cây DFS (Spanning Tree) với đồ thị ví dụ

Đồ thị vô hướng có trọng số:

```text
A --9-- B
A --6-- D
B --19- D
B --7-- E
E --29- H
A --8-- H
A --3-- C
C --6-- F
```

Ta sẽ duyệt **DFS (Depth-First Search)** bắt đầu từ đỉnh `A` và xây dựng **cây DFS (spanning tree)** tương ứng.

---

## 1. Ý tưởng của DFS

DFS là duyệt **ưu tiên đi sâu**:

1. Bắt đầu từ một đỉnh xuất phát (ở đây là `A`), đánh dấu là **đã thăm**.
2. Chọn **một đỉnh kề chưa thăm** → đi tiếp sang đó.
3. Lặp lại: từ đỉnh hiện tại, lại chọn một đỉnh kề chưa thăm để đi tiếp.
4. Nếu một đỉnh **không còn đỉnh kề chưa thăm**, ta **quay lui (backtrack)** về đỉnh trước đó.
5. Làm tiếp cho đến khi **không còn đỉnh nào chưa thăm**.

Mỗi lần ta đi từ đỉnh `u` sang đỉnh `v` lần đầu tiên, ta **thêm cạnh `(u, v)` vào cây DFS**.

> Lưu ý: Thứ tự duyệt phụ thuộc vào **thứ tự danh sách kề** (ví dụ: theo alphabet, hoặc theo thứ tự thêm cạnh).

Trong ví dụ này, giả sử ta lưu danh sách kề theo **thứ tự alphabet tăng dần**.

---

## 2. Danh sách kề (giả sử theo alphabet)

Từ các cạnh đã cho, ta suy ra (không quan tâm trọng số trong DFS):

```text
A: B, C, D, H
B: A, D, E
C: A, F
D: A, B
E: B, H
F: C
H: A, E
```

Khi duyệt DFS từ `A`, ta sẽ xét các đỉnh kề của mỗi đỉnh theo đúng thứ tự trên.

---

## 3. Các bước duyệt DFS từ A

Ký hiệu:
- `Visited`: tập các đỉnh đã thăm
- `Tree edges`: các cạnh thuộc cây DFS

### Bước 0 – Khởi tạo

- `Visited = {}` (rỗng)
- Bắt đầu DFS(`A`)

---

### Bước 1 – Thăm A

- `Visited = {A}`
- Cạnh cây: chưa có cạnh vì đây là đỉnh bắt đầu
- Láng giềng A: **B, C, D, H** (xét lần lượt)

Chọn đỉnh đầu tiên chưa thăm là **B** → đi từ `A` sang `B`.

- Thêm cạnh `(A, B)` vào cây DFS.

`Tree edges = {(A, B)}`

Gọi đệ quy/tiếp tục DFS tại `B`.

---

### Bước 2 – Từ B

- `Visited = {A, B}`
- Láng giềng B: **A, D, E**

Lần lượt xét:
1. `A` – đã thăm → bỏ qua
2. `D` – **chưa thăm** → đi từ `B` sang `D`

- Thêm cạnh `(B, D)` vào cây DFS

`Tree edges = {(A, B), (B, D)}`

Tiếp tục DFS tại `D`.

---

### Bước 3 – Từ D

- `Visited = {A, B, D}`
- Láng giềng D: **A, B**

1. `A` – đã thăm
2. `B` – đã thăm

Không còn láng giềng nào chưa thăm → **quay lui** về `B`.

---

### Bước 4 – Quay lại B, xét tiếp

Ta đang ở `B`, đã xét xong `D`, tiếp tục xét láng giềng tiếp theo:

- Láng giềng B: **A, D, E**
  - `A` – đã thăm
  - `D` – đã thăm
  - `E` – **chưa thăm** → đi từ `B` sang `E`

- Thêm cạnh `(B, E)` vào cây DFS

`Tree edges = {(A, B), (B, D), (B, E)}`

DFS tại `E`.

---

### Bước 5 – Từ E

- `Visited = {A, B, D, E}`
- Láng giềng E: **B, H**

1. `B` – đã thăm
2. `H` – **chưa thăm** → đi từ `E` sang `H`

- Thêm cạnh `(E, H)` vào cây DFS

`Tree edges = {(A, B), (B, D), (B, E), (E, H)}`

DFS tại `H`.

---

### Bước 6 – Từ H

- `Visited = {A, B, D, E, H}`
- Láng giềng H: **A, E**
  - `A` – đã thăm
  - `E` – đã thăm

Không còn láng giềng chưa thăm → **quay lui** về `E`, rồi về `B`, rồi về `A`
(vì B cũng hết láng giềng mới, E cũng vậy).

---

### Bước 7 – Quay lại A, xét tiếp

Ta quay lại `A`, lúc này đã xét xong `B`, tiếp tục xét danh sách kề `A: B, C, D, H`:

- `B` – đã thăm
- `C` – **chưa thăm** → đi từ `A` sang `C`

- Thêm cạnh `(A, C)` vào cây DFS

`Tree edges = {(A, B), (B, D), (B, E), (E, H), (A, C)}`

DFS tại `C`.

---

### Bước 8 – Từ C

- `Visited = {A, B, C, D, E, H}`
- Láng giềng C: **A, F**
  - `A` – đã thăm
  - `F` – **chưa thăm** → đi từ `C` sang `F`

- Thêm cạnh `(C, F)` vào cây DFS

`Tree edges = {(A, B), (B, D), (B, E), (E, H), (A, C), (C, F)}`

DFS tại `F`.

---

### Bước 9 – Từ F

- `Visited = {A, B, C, D, E, F, H}`
- Láng giềng F: **C**
  - `C` – đã thăm

Không còn láng giềng chưa thăm → quay lui về `C` → `A`.

Ở `A`, ta xét tiếp:

- `D` – đã thăm (qua nhánh B)
- `H` – đã thăm (qua nhánh E)

Không còn đỉnh chưa thăm → **kết thúc DFS**.

---

## 4. Cây DFS thu được

Các cạnh thuộc cây DFS (spanning tree) là:

```python
[
    ('A', 'B', 9),
    ('B', 'D', 19),
    ('B', 'E', 7),
    ('E', 'H', 29),
    ('A', 'C', 3),
    ('C', 'F', 6)
]
```

(Trọng số không ảnh hưởng đến DFS, chỉ được giữ lại cho đẹp theo đề bài.)

Tập đỉnh: `{A, B, C, D, E, F, H}` → có đúng `n - 1 = 6` cạnh → đây là **một cây khung (spanning tree)** hợp lệ của đồ thị.

---

## 5. Vẽ cây DFS (ASCII)

Có nhiều cách vẽ, dưới đây là một cách dễ nhìn, gốc là `A`:

```text
        A
      /   \
     B     C
   /   \    \
  D     E    F
         \
          H
```

Hoặc thể hiện dạng cây thụt lề theo thứ tự duyệt DFS:

```text
A
├── B
│   ├── D
│   └── E
│       └── H
└── C
    └── F
```

Mỗi nhánh đi xuống là **đường đi sâu** theo DFS.  
Khi không đi sâu thêm được nữa, ta **quay lui** và rẽ sang nhánh khác.

---

## 6. So sánh nhanh với Minimum Spanning Tree (MST)

- **Cây DFS**: phụ thuộc vào **thứ tự duyệt đỉnh kề**, *không quan tâm trọng số*.
- **Cây MST (ví dụ dùng Prim)**: phụ thuộc vào **trọng số cạnh**, luôn cố gắng chọn **cạnh nhẹ nhất** để tổng trọng số nhỏ nhất.

Trong chương trình của bạn:
- `spanning_tree_dfs(g, start="A")` → cho ra **cây DFS**
- `prim_mst(g, start="A")` → cho ra **cây khung nhỏ nhất (MST)**

Hai cây này **thường khác nhau**, và điều đó là hoàn toàn bình thường.

---

## 7. Gợi ý chèn hình minh họa vào README

Nếu bạn vẽ cây DFS bằng tay (hoặc dùng draw.io, Excalidraw, PowerPoint, v.v.) và lưu thành file `dfs_tree.png`,  
bạn có thể chèn vào README như sau:

```markdown
![DFS Spanning Tree](dfs_tree.png)
```

Khi mở repo trên GitHub, hình cây DFS sẽ hiển thị trực tiếp trong README.

---

Chúc bạn học tốt phần **Tree & Spanning Tree** trong Toán Rời Rạc! ✨
