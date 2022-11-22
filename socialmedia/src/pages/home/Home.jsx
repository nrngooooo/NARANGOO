import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import "./Home.css"
import { useState, useEffect } from "react";
import { sendRequest, urlLookup } from "../../settings/settings"
export default function Home() {

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
        <h5><button onClick={() => console.log(gazar.chiglelnum)}>
          {gazar.chiglelname}</button>
        </h5>
        <br />
      </div>
    )
  });

  return (
    <>
      {DisplayData}
      <p>{datas && JSON.stringify(datas)}</p>
      <Topbar sum={datas && datas.data[9].sumduud[3]['sumname']} />
      <div className="homeContainer">
        <Sidebar />
        <Feed />
        <Rightbar />
      </div>
    </>
  )
}