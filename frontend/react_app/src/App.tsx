import { Switch, Route, BrowserRouter as Router } from "react-router-dom";
import { PaySeller } from "./PaySeller/PaySeller";
import { Seller } from "./Seller/Seller";

function App() {
  return (
    <Router>
      <Switch>
        <Route
          path="/pay/:sellerHandle"
          render={({ match }) => (
            <PaySeller sellerHandle={match.params.sellerHandle} />
          )}
        />
        <Route
          path="/seller/:sellerId"
          render={({ match }) => <Seller sellerId={match.params.sellerId} />}
        />
      </Switch>
    </Router>
  );
}

export default App;
