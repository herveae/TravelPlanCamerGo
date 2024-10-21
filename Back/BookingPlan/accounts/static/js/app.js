const main= document.getElementById("main")

const checkbox = document.getElementById("checkbox")
checkbox.addEventListener("change", () => {
  document.body.classList.toggle("dark")
  main.classList.toggle("dark")
})