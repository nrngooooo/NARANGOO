import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import "./Home.css"
import { useState, useEffect} from "react";
import {sendRequest, urlLookup} from "../../settings/settings"
export default function Home() {

  const [datas, setDatas] = useState();

  useEffect(() => {
    const bodyChiglel = {
      action: "chiglel",
    };

    sendRequest(urlLookup, bodyChiglel).then((data) => setDatas(data));
  },[]);
  return (
    <>
    <p>{datas && JSON.stringify(datas)[9]["sumduud"]}</p>
      <Topbar />
      <div className="homeContainer">
        <Sidebar />
        <Feed />
        <Rightbar />
      </div>
    </>
  )
}