import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import "./Home.css"
import { useState, useEffect } from "react";
import { sendRequest, urlLookup } from "../../settings/settings"
import { Button, notification } from 'antd';

export default function Home() {
  const openNotification = ((title,desc) => {
    notification.open({
      message: title,
      description: desc,
      onClick: () => {
        console.log(desc+'Clicked!');
      },
    });
  });
  const [datas, setDatas] = useState();

  useEffect(() => {
    const bodyChiglel = {
      action: "chiglel",
    };

    sendRequest(urlLookup, bodyChiglel).then((data) => setDatas(data));
  }, []);
    const DisplayData = datas && datas.data.map((gazar) => {
      return (
        <div key={gazar.chiglelnum}>
          <h5><Button type="primary" onClick={()=>openNotification(gazar.chiglelnum,gazar.chiglelname)}>{gazar.chiglelnum}. 
            {gazar.chiglelname}</Button>
          </h5>
          <br />
        </div>
      )
  });

  return (
    <>
      {DisplayData}
      <p>{datas && JSON.stringify(datas)}</p>
      <Topbar/>
      <div className="homeContainer">
        <Sidebar />
        <Feed />
        <Rightbar />
      </div>
    </>
  )
}