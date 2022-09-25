import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import "./profile.css"

export default function Profile() {
  return (
    <>
    <Topbar/>
    <div className="profile">
      <Sidebar/>
      <div className="profileRight">
        <div className="profileRightTop">hhgh</div>
        <div className="profileRightBottom">
            <Feed/>  
            <Rightbar/>
        </div>
      </div>
    </div>
    </>
  )
}
