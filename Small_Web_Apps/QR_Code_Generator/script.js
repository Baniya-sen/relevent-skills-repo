document.addEventListener('DOMContentLoaded', () => {
    let imageBox = document.getElementById('img-box');
    let image = document.getElementById('qrImage');

    document.getElementById('submit').addEventListener('click', () => {
        let text = document.getElementById('qrText');
        if (text.value.length > 0) {
            imageBox.classList.add('show-img');
            image.src = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=" + text.vale;
        } else {
            text.classList.add('error');
            setTimeout(()=>{
                text.classList.remove('error');
            },400);
        }
    });
});
