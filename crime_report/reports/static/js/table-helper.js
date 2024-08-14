document.addEventListener('DOMContentLoaded', function() {
    // Automatically add 'sortable' class to all headers
    document.querySelectorAll('table th').forEach(th => th.classList.add('sortable'));

    // Debounce function to limit the rate at which a function is executed
    function debounce(func, wait = 300) {
        let timeout;
        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    // Show spinner
    function showSpinner() {
        document.getElementById('spinner').style.display = 'block';
    }

    // Hide spinner
    function hideSpinner() {
        document.getElementById('spinner').style.display = 'none';
    }

    // Create a new Web Worker for filtering
    const filterWorker = new Worker(filterWorkerPath);

    filterWorker.onmessage = function(event) {
        const filteredRows = event.data;
        const tableBody = document.querySelector('table tbody');
        tableBody.innerHTML = ''; // Clear current table rows
        filteredRows.forEach(rowData => {
            if (rowData) {
                const row = document.createElement('tr');
                rowData.forEach(cellData => {
                    const cell = document.createElement('td');
                    cell.textContent = cellData;
                    row.appendChild(cell);
                });
                tableBody.appendChild(row);
            }
        });
        hideSpinner(); // Hide the spinner when done
    };

    // Add filter inputs to each column
    const headerRow = document.querySelector('table thead tr');
    const filterRow = document.createElement('tr');
    const rowsData = Array.from(document.querySelectorAll('table tbody tr')).map(row => 
        Array.from(row.children).map(cell => cell.textContent)
    );

    headerRow.querySelectorAll('th').forEach((th, index) => {
        const filterCell = document.createElement('th');
        const fieldDiv = document.createElement('div');
        fieldDiv.classList.add('field');

        const input = document.createElement('input');
        input.type = 'text';
        input.placeholder = 'Filter...';
        input.classList.add('filter-input');

        const lineDiv = document.createElement('div');
        lineDiv.classList.add('line');

        fieldDiv.appendChild(input);
        fieldDiv.appendChild(lineDiv);
        filterCell.appendChild(fieldDiv);
        filterRow.appendChild(filterCell);

        // Add filtering functionality with debounce
        input.addEventListener('input', debounce(function() {
            showSpinner();
            filterWorker.postMessage({
                rowsData: rowsData,
                filterValue: this.value,
                columnIndex: index
            });
        }));
    });

    // Insert the filter row right after the header row
    headerRow.parentNode.insertBefore(filterRow, headerRow.nextSibling);

    // Sorting functionality
    const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;
    const comparer = (idx, asc) => (a, b) => ((v1, v2) => 
        v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
    )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

    document.querySelectorAll('th.sortable').forEach(th => th.addEventListener('click', function() {
        const table = th.closest('table');
        const tbody = table.querySelector('tbody');
        Array.from(tbody.querySelectorAll('tr'))
            .sort(comparer(Array.from(th.parentNode.children).indexOf(th), this.asc = !this.asc))
            .forEach(tr => tbody.appendChild(tr));

        // Remove existing sort indicators from other headers
        document.querySelectorAll('th').forEach(header => header.classList.remove('sorted-asc', 'sorted-desc'));

        // Add sort indicator to the clicked header
        th.classList.toggle('sorted-asc', this.asc);
        th.classList.toggle('sorted-desc', !this.asc);
    }));
});
