const tableData = async () => {
  var url = "https://jsonplaceholder.typicode.com/todos/" ; 
  var url = "https://app-service-recruiter.azurewebsites.net/core/api/v1/candidate/" ; 
  const response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  var data = await response.json();
  console.log("NEw Data=> ", data);
  return data;
};


