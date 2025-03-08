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
import { Modal, Box, List, ListItem, ListItemText } from "@mui/material";

import parkingFines from './fines.json'

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 600,
  bgcolor: "whitesmoke",
  borderRadius: "5px",
  border: "1px solid #a9aaad",

  boxShadow: 24,
  p: 4,
};

const columns = [{ field: "permit", headerName: "Permit Name", width: 350 }];

const rows = [
  { id: 1, permit: "17FAE" },
  { id: 2, permit: "18-19FAE" },
  { id: 3, permit: "19-20FAE" },
  { id: 4, permit: "4H" },
  { id: 5, permit: "A" },
  { id: 6, permit: "AA" },
  { id: 7, permit: "AE" },
  { id: 8, permit: "After Hours" },
  { id: 9, permit: "All Campus" },
  { id: 10, permit: "All Permits" },
  { id: 11, permit: "Alumni" },
  { id: 12, permit: "B" },
  { id: 13, permit: "BB" },
  { id: 14, permit: "Breaksgiving" },
  { id: 15, permit: "Bundle Pack-FS" },
  { id: 16, permit: "Bundle Pack-Student" },
  { id: 17, permit: "Bus Bundle Pack" },
  { id: 18, permit: "C" },
  { id: 19, permit: "Campus Meter" },
  { id: 20, permit: "Carpool" },
  { id: 21, permit: "CC" },
  { id: 22, permit: "Courier" },
  { id: 23, permit: "Daily Service Permit (Paper)" },
  { id: 24, permit: "DD" },
  { id: 25, permit: "E" },
  { id: 26, permit: "EE" },
  { id: 27, permit: "EMBA" },
  { id: 28, permit: "Emeritus" },
  { id: 29, permit: "ER" },
  { id: 30, permit: "Everyone" },
  { id: 31, permit: "F" },
  { id: 32, permit: "Faculty Staff Green Permit" },
  { id: 33, permit: "FAE" },
  { id: 34, permit: "FF" },
  { id: 35, permit: "FS Summer" },
  { id: 36, permit: "G" },
  { id: 37, permit: "Gate Card" },
  { id: 38, permit: "GG" },
  { id: 39, permit: "Golden ID" },
  { id: 40, permit: "Green Permit-Student" },
  { id: 41, permit: "H" },
  { id: 42, permit: "HC" },
  { id: 43, permit: "HH" },
  { id: 44, permit: "HP" },
  { id: 45, permit: "II" },
  { id: 46, permit: "J" },
  { id: 47, permit: "JJ" },
  { id: 48, permit: "K" },
  { id: 49, permit: "KK" },
  { id: 50, permit: "L" },
  { id: 51, permit: "LL" },
  { id: 52, permit: "Lot 1" },
  { id: 53, permit: "Lot 10" },
  { id: 54, permit: "Lot 11 Commuter" },
  { id: 55, permit: "Lot 15" },
  { id: 56, permit: "Lot 16" },
  { id: 57, permit: "Lot 19" },
  { id: 58, permit: "Lot 2" },
  { id: 59, permit: "Lot 3" },
  { id: 60, permit: "Lot 3 Commuter" },
  { id: 61, permit: "Lot 4" },
  { id: 62, permit: "Lot 6 Commuter" },
  { id: 63, permit: "Lot 6 Resident" },
  { id: 64, permit: "Lot 8" },
  { id: 65, permit: "Lot 9" },
  { id: 66, permit: "Lot V - Anacostia" },
  { id: 67, permit: "Lot V - Artemesia/Cypress" },
  { id: 68, permit: "M" },
  { id: 69, permit: "MC" },
  { id: 70, permit: "MD" },
  { id: 71, permit: "Medical-FS" },
  { id: 72, permit: "Medical-Student" },
  { id: 73, permit: "Micromobility" },
  { id: 74, permit: "MM" },
  { id: 75, permit: "Motorcycle" },
  { id: 76, permit: "N" },
  { id: 77, permit: "NN" },
  { id: 78, permit: "No Permits" },
  { id: 79, permit: "O" },
  { id: 80, permit: "OO" },
  { id: 81, permit: "Overnight Storage-Lot 11" },
  { id: 82, permit: "Overnight Storage-Lot 16" },
  { id: 83, permit: "Overnight Storage-Lot 17" },
  { id: 84, permit: "Overnight Storage-Lot 19" },
  { id: 85, permit: "P" },
  { id: 86, permit: "Paper Service" },
  { id: 87, permit: "PH" },
  { id: 88, permit: "PP" },
  { id: 89, permit: "Q" },
  { id: 90, permit: "QQ" },
  { id: 91, permit: "Quarantine" },
  { id: 92, permit: "R" },
  { id: 93, permit: "RR" },
  { id: 94, permit: "S" },
  { id: 95, permit: "SA" },
  { id: 96, permit: "Scooter/MC" },
  { id: 97, permit: "SDStar" },
  { id: 98, permit: "Service Permit" },
  { id: 99, permit: "Short Term Parking" },
  { id: 100, permit: "SLL" },
  { id: 101, permit: "SS" },
  { id: 102, permit: "Stadium Drive Garage" },
  { id: 103, permit: "Student Lot B" },
  { id: 104, permit: "Student Lot U" },
  { id: 105, permit: "Student Lot UU" },
  { id: 106, permit: "Student Lot XX" },
  { id: 107, permit: "Student TV" },
  { id: 108, permit: "Summer Commuter" },
  { id: 109, permit: "Summer Resident" },
  { id: 110, permit: "Surface Lot" },
  { id: 111, permit: "T" },
  { id: 112, permit: "Time and Materials" },
  { id: 113, permit: "TMP" },
  { id: 114, permit: "TT" },
  { id: 115, permit: "TV" },
  { id: 116, permit: "U" },
  { id: 117, permit: "UU" },
  { id: 118, permit: "V" },
  { id: 119, permit: "Visitor After Hours" },
  { id: 120, permit: "VM" },
  { id: 121, permit: "W" },
  { id: 122, permit: "WW" },
  { id: 123, permit: "X" },
  { id: 124, permit: "XX" },
  { id: 125, permit: "Y" },
  { id: 126, permit: "YC" },
  { id: 127, permit: "YY" },
  { id: 128, permit: "Z" },
];



const paginationModel = { page: 0, pageSize: 5 };

export default function App() {
  const [date, setDate] = useState(null);
  const [time, setTime] = useState(null);
  const [perms, setPerms] = useState(null);
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

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
          window.alert(response.data.Lots);
        })
        .catch((err) => console.error(err));
    }
  }, [date, time, perms]);

  if (!lots) return [];

  const handleSelectionChange = (selectionModel) => {
    const selectedPerms = selectionModel.map((id) =>
      rows.find((row) => row.id === id)
    );
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
              <a
                href="https://transportation.umd.edu/parking"
                style={{ width: "43%", marginRight: "1vw" }}
                target="_blank"
                rel="noreferrer"
              >
                <Button
                  variant="contained"
                  sx={{
                    backgroundColor: "red",
                    width: "100%",
                  }}
                  startIcon={<LuClipboardList />}
                >
                  Parking Rules
                </Button>
              </a>

              <Button
                variant="contained"
                sx={{ backgroundColor: "red", width: "43%" }}
                startIcon={<MdAttachMoney />}
                onClick={handleOpen}
              >
                Parking Fines
              </Button>
              <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
              >
                <Box sx={style}>
                  <h1>Parking Fines</h1>
                  <List
                    sx={{
                      maxHeight: 200, 
                      overflow: "auto", 
                    }}
                  >
                    {parkingFines.map((fine, index) => (
                      <ListItem key={index}>
                        <ListItemText
                          primary={`${fine.code} - ${fine.amount}`}
                          secondary={fine.description}
                        />
                      </ListItem>
                    ))}
                  </List>
                </Box>
              </Modal>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
