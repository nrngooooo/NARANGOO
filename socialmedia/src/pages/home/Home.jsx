import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import "./Home.css"
import { useState, useEffect } from "react";
import { sendRequest, urlLookup } from "../../settings/settings"
import { Button, notification } from 'antd';
import { resp } from "../../getdata/dummy";

export default function Home() {
  const openNotification = ((title, desc) => {
    notification.open({
      message: title,
      description: desc,
      onClick: () => {
        console.log(desc + 'Clicked!');
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
        <h5><Button type="primary" onClick={() => openNotification(gazar.chiglelnum, gazar.chiglelname)}>{gazar.chiglelnum}.
          {gazar.chiglelname}</Button>
        </h5>
        <br />
      </div>
    )
  });
  // let friendsList = datas && datas.data.friends.map((items) => {
  //   return (
  //     <li className="sidebarFriend">
  //       <img className="sidebarFriendImg" src={items.friendphoto} alt=""></img>
  //       <span className="sidebarFriendName">{items.friendname}</span>
  //     </li>
  //   );
  // })

  return (
    <>
      {JSON.stringify(resp)}
      {DisplayData}
      <p>{datas && JSON.stringify(datas)}</p>
      {/* {friendsList} */}
      <Topbar ilgeesen={(resp)} />
      <div className="homeContainer">
        <Sidebar />
        <Feed />
        <Rightbar />
      </div>
    </>
  )
}