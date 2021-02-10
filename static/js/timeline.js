const dropdown = document.getElementById("dropdown");
const settings = document.getElementsByClassName("setting");

for(setting of settings){
	setting.addEventListener("click", (event) => {
		event.currentTarget.parentNode.children[2].classList.toggle("hidden");
	})
}