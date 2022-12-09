import "./sidebar.css"
import { Users } from "../../dummyData"
import CloseFriend from "../closeFriend/CloseFriend"
import { RssFeed, PlayCircleOutline, Group, Bookmark, HelpOutline, WorkOutline, Event, School } from "@mui/icons-material"

export default function Sidebar({ friends }) {
  const friendsList = friends.friends.map((items) => {
    return (
      <li className="sidebarFriend">
        <img className="sidebarFriendImg" src={items.friendphoto} alt=""></img>
        <span className="sidebarFriendName">{items.friendname}</span>
      </li>
    );
  })
  return (
    <div className="sidebar">
      {/* {JSON.stringify(friends)} */}
      <div className="sidebarWrapper">
        <ul className="sidebarList">
          <li className="sidebarListItem">
            <RssFeed className="sidebarIcon" />
            <span className="sidebarListItemText">Feed</span>
          </li>
          <li className="sidebarListItem">
            <PlayCircleOutline className="sidebarIcon" />
            <span className="sidebarListItemText">Videos</span>
          </li>
          <li className="sidebarListItem">
            <Group className="sidebarIcon" />
            <span className="sidebarListItemText">Group</span>
          </li>
          <li className="sidebarListItem">
            <Bookmark className="sidebarIcon" />
            <span className="sidebarListItemText">Bookmarks</span>
          </li>
          <li className="sidebarListItem">
            <HelpOutline className="sidebarIcon" />
            <span className="sidebarListItemText">Questions</span>
          </li>
          <li className="sidebarListItem">
            <WorkOutline className="sidebarIcon" />
            <span className="sidebarListItemText">Jobs</span>
          </li>
          <li className="sidebarListItem">
            <Event className="sidebarIcon" />
            <span className="sidebarListItemText">Events</span>
          </li>
          <li className="sidebarListItem">
            <School className="sidebarIcon" />
            <span className="sidebarListItemText">Courses</span>
          </li>
          <button className="sidebarButton">Show More</button>
          <hr className="sidebarHr" />
          <ul className="sidebarFriendList">
          {friendsList}
            {Users.map((u) => (
              <CloseFriend key={u.id} user={u} />
            ))}
          </ul>
        </ul>
      </div>
    </div>
  )
}
