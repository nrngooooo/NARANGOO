import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import "./Home.css"
import { useState, useEffect} from "react";

export default function Home() {

  const [datas, setDatas] = useState();

  useEffect(() => {
    const urlLookup = "http://btax.mandakh.org:8000/lookup/";

    const bodyChiglel = {
      action: "chiglel",
    };

    sendRequest(urlLookup, bodyChiglel).then((data) => setDatas(data));
  },[]);


  const sendRequest = async (url, body) => {
    try {
      let response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        throw "Something went wrong.";
      }
      let data = await response.json();

      // Log the data to the console
      // console.log(data);
      return data;
    } catch (error) {
      console.warn(error);
    }
  };
  return (
    <>
    <p>{datas}</p>
      <Topbar />
      <div className="homeContainer">
        <Sidebar />
        <Feed />
        <Rightbar />
      </div>
    </>
  )
}
