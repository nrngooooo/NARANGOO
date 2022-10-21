import styled from "styled-components";
import { useStates } from "react";
import { FaSearch } from "react-icons/fa";

function Search() {
  return (
    <form>
        <input type="text" />
    </form>
  )
}

const FormStyle = styled.form`
    margin: 0rem 20rem;
    position: relative;
`

export default Search