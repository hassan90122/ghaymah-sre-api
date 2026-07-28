const API_URL =
"https://ghaymah-sre-api-20e343cababc.hosted.ghaymah.systems";


async function checkApplication(){

    try {

        let start = Date.now();


        let healthResponse =
            await fetch(API_URL + "/health");


        let end = Date.now();


        let responseTime =
            end - start;



        let statsResponse =
            await fetch(API_URL + "/stats");


        let stats =
            await statsResponse.json();



        document.getElementById("status").innerHTML =
            healthResponse.ok ? "UP" : "DOWN";


        document.getElementById("response").innerHTML =
            responseTime + " ms";


        document.getElementById("requests").innerHTML =
            stats.requests;



    }

    catch(error){

        document.getElementById("status").innerHTML =
            "DOWN";

        console.log(error);

    }

}



checkApplication();


setInterval(
    checkApplication,
    30000
);
