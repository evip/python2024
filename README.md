# Python_2024

<h1>Sinh viên học Python thông qua các vấn đề sau.</h1>

<h2>Vấn đề 1: Định giá Quyền chọn theo mô hình Black-Scholes</h2>


<h2>Vấn đề 2: Tìm điểm cân bằng Nash trong lý thuyết trò chơi</h2>
<h3>Cạnh tranh định giá trong một thị trường độc quyền nhóm</h3>
<p>Giả sử có hai công ty A và B cùng sản xuất một loại sản phẩm tương tự (ví dụ: nước giải khát) và phải quyết định về giá bán sản phẩm. Mỗi công ty đều muốn tối đa hóa lợi nhuận. Lợi nhuận này phụ thuộc vào lựa chọn giá của cả hai. Nếu một công ty định giá quá cao so với đối thủ, họ có nguy cơ mất thị phần. Ngược lại, nếu định giá quá thấp để hút khách, họ có thể giảm biên lợi nhuận.</p>

<p>Trong mô hình đơn giản, hai công ty có thể đưa ra hai mức giá: Cao (H) hoặc Thấp (L). Mỗi sự kết hợp (A chọn H/L, B chọn H/L) sẽ dẫn đến một cặp lợi nhuận khác nhau. Chúng ta có thể biểu diễn kết quả này thông qua một bảng payoff.</p>

<table>
<tr>
    <td></td>
    <td><b>B: Cao (H)	</b></td>
    <td><b>B: Thấp (L)</b></td>
</tr>
<tr>
    <td><b>A: Cao (H)</b></td>
    <td>A: 20, B: 20</td>
    <td>A: 5, B: 25</td>
</tr>
<tr>
    <td><b>A: Thấp (L)</b></td>
    <td>A: 25, B: 5</td>
    <td>A: 10, B: 10</td>
</tr>
</table>
<ul>
    <li>Khi cả hai chọn giá Cao, mỗi bên bán được ít nhưng với lợi nhuận trên đơn vị cao hơn, thu về lợi nhuận trung bình (20,20).</li>
    <li>Khi A chọn Cao, B chọn Thấp, B thu hút khách hàng về phía mình nên B được 25, A chỉ được 5. Tương tự khi A chọn Thấp, B chọn Cao thì A được 25, B được 5.</li>
    <li>Khi cả hai cùng chọn Thấp, giá rẻ hơn nên lợi nhuận biên thấp, họ chia thị phần tương đối đều, mỗi bên được 10.</li>
</ul>


