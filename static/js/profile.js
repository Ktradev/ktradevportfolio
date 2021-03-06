const dropdown = document.getElementById("dropdown");
const settings = document.getElementsByClassName("setting");

for(setting of settings){
	setting.addEventListener("click", (event) => {
		event.currentTarget.parentNode.children[3].classList.toggle("hidden");
	})
}