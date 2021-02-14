const cta = document.getElementById("cta");
const moon = document.getElementById("moon");
const body = document.getElementsByTagName("body")[0];

moon.addEventListener("click", () => {
	moon.children[0].classList.toggle("fas");
	moon.children[0].classList.toggle("far");
	if(moon.children[0].classList.contains("far")){
		cta.style.color = "white";
		cta.style.backgroundColor = "#395550";
		body.classList.remove("night");
		body.classList.add("day");
		moon.children[0].style.color = "#395550";
	}
	else{
		cta.style.color = "#395550";
		cta.style.backgroundColor = "white";
		body.classList.remove("day");
		body.classList.add("night");
		moon.children[0].style.color = "white";
	}
})