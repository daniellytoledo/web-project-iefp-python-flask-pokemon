// =====================================================
// Confirmação de exclusão de card
// =====================================================

document.addEventListener("DOMContentLoaded", function () {
    const formEliminar = document.getElementById("form_eliminar");

    if (formEliminar) {
        formEliminar.addEventListener("submit", function (evento) {
            const confirmado = window.confirm(
                "Tem certeza que deseja eliminar este Pokémon? Essa ação não pode ser desfeita."
            );

            if (!confirmado) {
                // Impede o envio do formulário se o usuário clicar em "Cancelar"
                evento.preventDefault();
            }
        });
    }
});