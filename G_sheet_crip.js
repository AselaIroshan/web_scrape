// Function to append a new row to a sheet
function appendRow(sheetName, rowData) {
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = spreadsheet.getSheetByName(sheetName);
    
    if (sheet !== null) {
      // Read existing data
      const existingData = sheet.getRange(1, 1, sheet.getLastRow(), 1).getValues().flat();
      
      // Check if the value already exists
      if (existingData.includes(rowData[0])) {
        return "Already exists";
      }
      
      // Append the new row
      sheet.appendRow(rowData[0]);
      return "Row added successfully";
    }
    
    return "Sheet not found";
  }
  
  // Main function to handle POST requests
  function doPost(e) {
    try {
      const path = e.parameter.path;
      const action = e.parameter.action;
      let debugInfo = `doPost called. Path: ${path}, Action: ${action}`;
  
      if (action === 'read') {
        const jsonData = json(path);
        return ContentService
              .createTextOutput(JSON.stringify({debugInfo, data: jsonData}))
              .setMimeType(ContentService.MimeType.JSON);
      } else if (action === 'write') {
        const rowData = JSON.parse(e.postData.contents).Users;
        
        let results = [];
        rowData.forEach(data => {
          const row = [
            data.timestamp || '',
            data.name || '',
            data.price || '',
            data.change || '',
            data.volume || '',
            data.signal || ''
          ];
          results.push(appendRow(path, [row]));
        });
        
        return ContentService
              .createTextOutput(`Results: ${results.join(", ")}. Debug: ${debugInfo}`)
              .setMimeType(ContentService.MimeType.TEXT);
      } else {
        return ContentService
              .createTextOutput(`Invalid action. Debug: ${debugInfo}`)
              .setMimeType(ContentService.MimeType.TEXT);
      }
    } catch (error) {
      return ContentService
            .createTextOutput(`An error occurred: ${error.toString()}`)
            .setMimeType(ContentService.MimeType.TEXT);
    }
  }
  