import React, { useEffect, useState } from 'react'


const WebSocketComponent = () => {
  const [logs, setLogs] = useState([])
  const [run,setRun]=useState(true)
  // let run = false;
  
  useEffect(() => {
    if(!run)return
    
    let ws = new WebSocket("ws://localhost:8000/ws/log/")
    // ws.close()
    ws.onmessage = (event) => {
      setLogs((prev) => [...prev, event.data]);
      console.log(event);
    }
    ws.onclose = () => {
      console.log("closed");
    }
    return () => {
      ws.close();
    }
  }, [run])
  // }
  return (
    <div className='socketbox'>
      <ul>
        {/* {logs} */}
          {logs.map((e) => {
            return <li>{JSON.parse(e).log}</li>
          })}
      </ul>
      <button onClick={()=>{setRun(!run)}}>{run ? "Pause" : "play"}</button>
    </div>
  )
}

export default WebSocketComponent