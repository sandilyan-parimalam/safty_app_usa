// filter-worker.js

self.onmessage = function(event) {
    const { rowsData, filterValue, columnIndex } = event.data;
    const filteredRows = rowsData.map(rowData => {
        const cellText = rowData[columnIndex].toLowerCase();
        const shouldDisplay = cellText.includes(filterValue.toLowerCase());
        return shouldDisplay ? rowData : null;
    });
    self.postMessage(filteredRows);
};
