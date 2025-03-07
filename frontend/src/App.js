import "./App.css";
import logo from "./Polka.png";
import { DataGrid } from "@mui/x-data-grid";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import { MdAttachMoney } from "react-icons/md";
import { LuClipboardList } from "react-icons/lu";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { DatePicker } from "@mui/x-date-pickers/DatePicker";
import { TimePicker } from "@mui/x-date-pickers/TimePicker";
import axios from "axios";


import { useState, useEffect } from "react";

const columns = [
  { field: "permit", headerName: "Permit Name", width: 350 },
];

const rows = [
  { id: 1, permit: "hi" },
  { id: 2, permit: "" },
  { id: 3, permit: "" },
  { id: 4, permit: "" },
  { id: 5, permit: "Targaryen" },
  { id: 6, permit: "Melisandre" },
  { id: 7, permit: "Clifford" },
  { id: 8, permit: "Frances" },
  { id: 9, permit: "Roxie" },
];

const paginationModel = { page: 0, pageSize: 5 };

export default function App() {
  const [date, setDate] = useState(null);
  const [time, setTime] = useState(null);
  const [perms, setPerms] = useState(null);


  const [lots, setLots] = useState([]);

  useEffect(() => {
    if (date && time && perms) {
      const queryParams = new URLSearchParams({
        date: date.format("YYYY-MM-DD"), 
        time: time.format("HH:mm"),
      });
  
      perms.forEach((p) => queryParams.append("permissions", p.permit)); 
  
      axios
        .get(`http://127.0.0.1:5000/?${queryParams.toString()}`)
        .then((response) => {
          setLots(response.data.Lots);
          window.alert(response.data.Lots)
        })
        .catch((err) => console.error(err));
    }
  }, [date, time, perms]);

  if (!lots) return [];

  const handleSelectionChange = (selectionModel) => {
    const selectedPerms = selectionModel.map((id) => rows.find((row) => row.id === id));
    setPerms(selectedPerms);
  };

  return (
    <div className="split">
      <div className="search">
        <div className="subSearch">
          <div className="center">
            <img src={logo} alt="logo" className="logo" />
          </div>
          <hr />
          <form>
            <div className="center">
              <LocalizationProvider dateAdapter={AdapterDayjs}>
                <DatePicker
                  label="Date"
                  value={date}
                  onChange={(newDate) => setDate(newDate)}
                  sx={{
                    backgroundColor: "white",
                    borderRadius: "5px",
                    width: "90%",
                  }}
                />
              </LocalizationProvider>
            </div>
            <div className="center">
              <LocalizationProvider dateAdapter={AdapterDayjs}>
                <TimePicker
                  label="Time"
                  value={time}
                  onChange={(newTime) => setTime(newTime)}
                  sx={{
                    backgroundColor: "white",
                    borderRadius: "5px",
                    width: "90%",
                  }}
                />
              </LocalizationProvider>
            </div>
            <div className="center">
              <Paper sx={{ height: "50vh", width: "90%" }}>
                <DataGrid
                  rows={rows}
                  columns={columns}
                  initialState={{ pagination: { paginationModel } }}
                  pageSizeOptions={[5, 10]}
                  checkboxSelection
                  onRowSelectionModelChange={handleSelectionChange}
                  sx={{ border: 0 }}
                />
              </Paper>
            </div>
            <div className="center">
              <Button
                variant="contained"
                sx={{
                  backgroundColor: "red",
                  marginRight: "1vw",
                  width: "43%",
                }}
                startIcon={<LuClipboardList />}
              >
                Parking Rules
              </Button>
              <Button
                variant="contained"
                sx={{ backgroundColor: "red", width: "43%" }}
                startIcon={<MdAttachMoney />}
              >
                Parking Fines
              </Button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
