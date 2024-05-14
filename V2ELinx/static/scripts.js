function showNext() {
    var select = document.getElementById('registerNo');
    var selectedIndex = select.selectedIndex;
    if (selectedIndex < select.options.length - 1) {
        select.selectedIndex = selectedIndex + 1;
    }
}

function showPrevious() {
    var select = document.getElementById('registerNo');
    var selectedIndex = select.selectedIndex;
    if (selectedIndex > 0) {
        select.selectedIndex = selectedIndex - 1;
    }
}

function sortTable(columnIndex, ascending) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("studentTable");
    switching = true;

    while (switching) {
        switching = false;
        rows = table.rows;

        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[columnIndex];
            y = rows[i + 1].getElementsByTagName("TD")[columnIndex];

            if (ascending) {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch= true;
                    break;
                }
            } else {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch= true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

window.onload = function() {
    var thElements = document.getElementsByTagName("th");
    for (var i = 0; i < thElements.length; i++) {
        thElements[i].addEventListener("click", function() {
            var columnIndex = this.cellIndex;
            var ascending = true;
            if (this.getAttribute("data-sorted") === "ascending") {
                ascending = false;
                this.setAttribute("data-sorted", "descending");
            } else {
                this.setAttribute("data-sorted", "ascending");
            }
            sortTable(columnIndex, ascending);
        });
    }
};

