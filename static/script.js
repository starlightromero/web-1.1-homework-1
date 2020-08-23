const button = document.getElementById('button')

const goHome = () => {
  console.log('clicked')
  window.location.href = '/'
}

button.addEventListener('click', goHome)
