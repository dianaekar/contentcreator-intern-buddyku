'use strict';

const modal = document.querySelector('.modal'); //Mendefinisikan Variabel modal
const overlay = document.querySelector('.overlay');  //Mendefinisikan Variabel overlay
const btnCloseModal = document.querySelector('.close-modal');  //Mendefinisikan Variabel btnCloseModal
const btnsOpenModal = document.querySelectorAll('.show-modal');  //Mendefinisikan Variabel btnsOpenModal

const openModal = function () {
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};  //Mendefinisikan Variabel openModal yang didalamnya di isi dengan ketentuan untuk 

const closeModal = function () {
  modal.classList.add('hidden'); //Menghapus class hidden pada variable modal (coba perhatikan dicode HTML)
  overlay.classList.add('hidden'); //Menghapus class hidden pada variable overlay (coba perhatikan dicode HTML)
};

for (let i = 0; i < btnsOpenModal.length; i++) // set loop untuk menampilkan Modal ketika di klik
  btnsOpenModal[i].addEventListener('click', openModal);

btnCloseModal.addEventListener('click', closeModal); // pendefinisian ketika modal di klik pada tanda x maka close
overlay.addEventListener('click', closeModal); // pendefinisian ketika klik pad bagian overlay modal akan close