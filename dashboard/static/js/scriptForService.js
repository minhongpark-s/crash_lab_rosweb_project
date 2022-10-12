var ros = new ROSLIB.Ros();
 
// rosbridge websocket server와의 연결을 생성합니다.
ros.connect('ws://0.0.0.0:9090');


ros.on('error', function (error) {
    console.log(error);
    document.getElementById('header').style.backgroundColor = "#f03737";
  });
   
  // 정상 연결
  ros.on('connection', function () {
    console.log('Connection made!');
    document.getElementById('header').style.backgroundColor = "#07a666";
  });
   
  // 연결 닫힘
  ros.on('close', function () {
    console.log('Connection closed.');
    document.getElementById('header').style.backgroundColor = "#a0a0a0";
  });

  var Client = new ROSLIB.Service({
    ros : ros,
    name : '/service_server',
    serviceType : 'ros_tutorials_service/srvTutorial',
  })

  document.getElementById("submit").onclick = function(){
    num1 = document.getElementById("firstNum").value;
    num2 = document.getElementById("secondNum").value;
    console.log(num1, num2);

    var sendNumbers = new ROSLIB.ServiceRequest({
        a: Number(num1),
        b: Number(num2)
    });

    Client.callService(sendNumbers, function(result){
        console.log(sendNumbers.a+ '+' + sendNumbers.b + "is " + result.result);
        document.getElementById('datashow').value = result.result;
    })

    console.log("finished");

  }


