// api url


// Defining async function
function getapi() {
const api_url = "http://127.0.0.1:5000/search/2";

	function callback(items) {
		console.log("callback --> ", items);
		console.log(items)
	}

	// Storing response
	fetch(api_url)
				.then(response => response.json())
				.then(json => {
					console.log("data --<> ", json)
					callback(json);
				}).catch(()=>{
					callback();
				});

}
// Calling that async function
getapi(api_url);

// Function to hide the loader
function hideloader() {
	document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
	let tab =
		`<tr>
		<th>Name</th>
		<th>Office</th>
		<th>Position</th>
		<th>Salary</th>
		</tr>`;

	// Loop to access all rows
	for (let r of data.list) {
		tab += `<tr>
	<td>${r.name} </td>
	<td>${r.office}</td>
	<td>${r.position}</td>
	<td>${r.salary}</td>		
</tr>`;
	}
	// Setting innerHTML as tab variable
	document.getElementById("employees").innerHTML = tab;
}
