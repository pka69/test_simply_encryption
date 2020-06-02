$(() => {
  $("#interest").on("change", e => {
    $("#interest-value").text(e.currentTarget.value + "%");
  });

  $("#timetable").DataTable({
    "language": {
      "lengthMenu": "Pokaż _MENU_ wyników na stronę",
      "zeroRecords": "Nic nie znaleziono",
      "info": "Strona _PAGE_ z _PAGES_",
      "infoEmpty": "Nic nie znaleziono",
      "infoFiltered": "(filtered from _MAX_ total records)",
      "paginate": {
        "first": "Pierwsza",
        "last": "Ostatnia",
        "next": "Następna",
        "previous": "Poprzednia"
      },
      "search": "Szukaj:",
    }
  });
});