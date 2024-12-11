# Python_2024

<h1>Sinh viên học Python thông qua các vấn đề sau.</h1>

<h2>Vấn đề 1: Định giá Quyền chọn theo mô hình Black-Scholes</h2>
<p>Mô hình Black-Scholes, còn được gọi là mô hình Black-Scholes-Merton, là một trong những mô hình nổi tiếng nhất trong tài chính toán học, được sử dụng để định giá các quyền chọn. Mô hình cung cấp một công thức tính giá lý thuyết cho quyền chọn mua (call option) và quyền chọn bán (put option) trên tài sản tài chính.</p>
<h3>Giới thiệu</h3>
<ul>
    <li><b>Mục tiêu:</b> Dự đoán giá trị quyền chọn bằng cách giả định rằng giá tài sản cơ sở (như cổ phiếu) thay đổi theo thời gian dựa trên một quá trình ngẫu nhiên.</li>
    <li><b>Đầu vào:</b> Các yếu tố ảnh hưởng đến giá trị quyền chọn:
        <ol>
            <li> $\ S_0$: Giá tài sản cơ sở hiện tại</li>
            <li>$\ K$: Giá thực hiện (strike price) của quyền chọn.</li>
            <li>$\ T$: Thời gian đến ngày đáo hạn </li>
            <li>$\ r$: Lãi suất phi rủi ro.</li>
            <li>$\ σ$: Độ biến động của giá tài sản.</li>
        </ol>
    </li>
    <li><b>Kết quả:</b> Giá trị quyền chọn mua ( $\ C_0$) hoặc quyền chọn bán ( $\ P_0$ ) tại thời điểm hiện tại.</li>
</ul>

<h3>Công thức Black-Scholes</h3>
<p>Công thức giá quyền chọn mua:</p>
<p text-align: center> $\ C_0 = S_0 * N(d_1) - K*e^{-r*T} * N(d_2) $</p>
<p>Công thức giá quyền chọn bán:</p>
<p text-align: center> $\ P_0 = K*e^{-rT} * N(-d_2) - S_0 * N(-d_1) $</p>
<ul>
    <li> $\ d_1 $ :    </li>
    <li>$\ d_2 = d_1 - σ * sqrt{T​} $ </li>
    <li>N(x): Hàm phân phối tích lũy chuẩn của phân phối chuẩn chuẩn hóa N(0,1).</li>
</ul>

<br>
<br>
<h2>Vấn đề 2: Tìm điểm cân bằng Nash trong lý thuyết trò chơi</h2>
<h3>2.1 Cạnh tranh định giá trong một thị trường độc quyền nhóm</h3>
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

<br>
<h3>2.2 Cạnh tranh lãi suất tiền gửi giữa hai ngân hàng</h3>
<p>Giả sử có hai ngân hàng lớn trên cùng địa bàn, Ngân hàng A và Ngân hàng B. Họ đang cố gắng thu hút nguồn vốn nhàn rỗi từ khách hàng bằng cách đưa ra lãi suất cho tiền gửi tiết kiệm kỳ hạn 12 tháng. Lợi nhuận của ngân hàng phần lớn đến từ chênh lệch lãi suất (huy động - cho vay). Tuy nhiên, để đơn giản hóa, ta xem xét khía cạnh thu hút khách hàng gửi tiền:</p>
<ul>
    <li>Cầu tiền gửi trên thị trường là hữu hạn (ví dụ: 100 tỷ đồng).
</li>
    <li>Nếu hai ngân hàng đưa ra lãi suất ngang nhau, họ chia đôi thị trường: mỗi bên huy động 50 tỷ đồng.</li>
    <li>Nếu một ngân hàng đưa ra lãi suất cao hơn, ngân hàng đó sẽ thu hút nhiều tiền gửi hơn (giả sử 70 tỷ đồng), trong khi ngân hàng còn lại chỉ được 30 tỷ đồng.</li>
    <li>Tuy nhiên, lãi suất cao hơn làm giảm biên lợi nhuận ngân hàng vì chi phí huy động tăng.</li>
</ul>

<p>Ví dụ, giả sử:</p>
<ul>
    <li>Lãi suất cho vay cố định mà ngân hàng có thể thực hiện là 8%/năm (để cho đơn giản).</li>
    <li>Ngân hàng phải trả lãi cho tiền gửi đúng bằng lãi suất họ công bố. Chi phí khác bỏ qua hoặc giả sử là không đáng kể.</li>
    <li>Hai mức lãi suất mà mỗi ngân hàng có thể chọn: 5% hoặc 7%.</li>
</ul>

<p>Cách tính lợi nhuận đơn giản</p>
<ul>
    <li>Lợi nhuận ≈ (Lãi cho vay - Lãi huy động) * Số tiền huy động được.</li>
    <li>Nếu lãi suất huy động là r%, lợi nhuận trên mỗi đồng là (8% - r%).</li>
    <li>Nếu một ngân hàng huy động D tỷ đồng, lợi nhuận = (8% - r%) * D (tính trên vốn huy động sau một năm, giả sử tỷ đơn giản).</li>
</ul>

<p><b>Thiết lập bài toán:</b></p>

<ol>
<li>Nếu cả hai chọn 5%:
    <ul>
        <li>Mỗi bên huy động 50 tỷ đồng.</li>
        <li>Lợi nhuận mỗi bên = (8% - 5%) * 50 tỷ = 3% * 50 tỷ = 1,5 tỷ.</li>
    </ul>
</li>

<li>Nếu A chọn 5%, B chọn 7%:
    <ul>
        <li>B có lãi suất cao hơn -> B huy động 70 tỷ, A huy động 30 tỷ.</li>
        <li>Lợi nhuận A = (8% - 5%) * 30 tỷ = 3% * 30 = 0,9 tỷ</li>
        <li>Lợi nhuận B = (8% - 7%) * 70 tỷ = 1% * 70 = 0,7 tỷ</li>
    </ul>
</li>


<li>Nếu A chọn 7%, B chọn 5% (tương tự trường hợp trên nhưng đổi vai):
    <ul>
        <li>A huy động 70 tỷ, B huy động 30 tỷ.</li>
        <li>Lợi nhuận A = (8% - 7%) * 70 tỷ = 1% * 70 = 0,7 tỷ</li>
        <li>Lợi nhuận B = (8% - 5%) * 30 tỷ = 3% * 30 = 0,9 tỷ</li>
    </ul>
</li>


<li>Nếu A chọn 7%, B chọn 7%:
    <ul>
        <li>Cả hai đều ra giá cao, chia đều 50-50.</li>
        <li>Lợi nhuận mỗi bên = (8% - 7%) * 50 tỷ = 1% * 50 = 0,5 tỷ.</li>
    </ul>
</li>

</ol>

<p>Bảng lợi nhuận</p>
<table>
<tr>
    <td></td>
    <td><b>B: 5% (Thấp)</b></td>
    <td><b>B: 7% (Cao)</b></td>
</tr>

<tr>
    <td><b>A: 5% (Thấp)</b></td>
    <td>A:1,5 tỷ, B:1,5 tỷ</td>
    <td>A:0,9 tỷ, B:0,7 tỷ</td>
</tr>

<tr>
    <td><b>A: 7% (Cao)</b></td>
    <td>A:0,7 tỷ, B:0,9 tỷ</td>
    <td>A:0,5 tỷ, B:0,5 tỷ</td>
</tr>
</table>

<p><b>Phân tích:</b></p>
<ul>
    <li>Tình huống (5%,5%) cho mỗi bên 1,5 tỷ. Nếu một bên chuyển từ 5% lên 7%, lợi nhuận của họ giảm xuống 0,7 tỷ hoặc 0,9 tỷ (so với 1,5 tỷ lúc ban đầu). Không có lợi.</li>
    <li>Tình huống (7%,7%) mỗi bên chỉ được 0,5 tỷ. Nếu một bên hạ về 5% thì họ sẽ được 0,9 tỷ (hoặc 1,5 tỷ nếu bên kia vẫn cố chấp 7%). Như vậy, từ (7%,7%) mỗi bên đều muốn hạ về 5% để tăng lợi nhuận. (7%,7%) không ổn định.</li>
</ul>

<p>Điểm cân bằng Nash trong ví dụ này chính là (5%,5%) vì:</p>
<ul>
    <li>Tại (5%,5%), không một ngân hàng nào có động lực tăng lãi suất lên 7% vì lợi nhuận sẽ giảm (từ 1,5 tỷ xuống 0,9 hoặc 0,7 tỷ).</li>
    <li>Như vậy, không ai muốn đổi chiến lược đơn phương.</li>
</ul>