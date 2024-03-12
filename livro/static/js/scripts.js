function mostra_form(form_id) {
  livro = document.getElementById('livro')
  categoria = document.getElementById('categoria')
  emprestimo = document.getElementById('emprestimo')
  modal_cadastro = document.getElementById('modal_cadastro')

  livro.style.display = 'none';
  categoria.style.display = 'none';
  emprestimo.style.display = 'none';

  if (form_id === 1) {
    modal_cadastro.innerText = `Cadastrar Livro`
    livro.style.display = 'block';
  } else if (form_id === 2) {
    modal_cadastro.innerText = `Cadastrar Categoria`
    categoria.style.display = 'block';
  } else if (form_id === 3) {
    modal_cadastro.innerText = `Fazer Emprestimo`
    emprestimo.style.display = 'block';
  }
}

// Rating Initialization
$(document).ready(function() {
  $('#rateMe2').mdbRate();
});

function insert_image(){
  id_img = document.getElementById('id_img')
  id_img.click()
}
function submit_image(){
  form = document.getElementById('form')
  form.submit()
}