function like() {

    var element = document.getElementById("count")
    var like = document.getElementById("like")
    if (like.className == "fa fa-heart-o") {
        like.className = "fa fa-heart"
        element_num = Number(element.innerText) + 1
        element.innerText = element_num
    } else {
        like.className = "fa fa-heart-o"
        element_num = Number(element.innerText) - 1
        element.innerText = element_num

    }
}


function submitt() {
    setTimeout(() => {
        console.log("dfdfdf")
        location.reload()
    }, 5000)
}