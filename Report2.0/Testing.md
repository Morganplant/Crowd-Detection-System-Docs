
Due to the nature of the Crowd Pulse project, I decided it would be best to use a blend of synthetic and real-world data. In accordance with the laws and regulations mentioned earlier in this report, I only used the crowd pulse system on network's I had direct authorization to do so.

Initially I tested the system a small home network, which did not accurately simulate the environment that the the project would be deployed in, i.e. large area networks that have high device counts. So to fix this I decided to use a python module named Faker,

Faker is a python package for generating fake data, it's useful for tasks, like database bootstrapping, documentation creation and data anonymization. I utilized faker to create synthetic data, I created data that simulated network topologies.

> [!warning] Go And Create the live aspects
> - Make it so that the topology moves and swaps as if there are people moving around

##### How was it tested?
As stated before initially the project was tested on small home networks, that I had access to at the time. Due to the nature of the project, I decided that testing on small home networks was not the best way to test the project, as it was built for crowd monitoring on a larger scale.

I thought of a different way to test the project, without access to a large scale network due to potential privacy and security issues. Synthetic data, this would allow me to create much larger data that I could use to test the system.

Using the Faker library allowed me to simulate various network environments realistically, This synthetic data generation approach provided a controlled yet expansive testing environment without compromising actual user data. By generating data representative of real-world network behaviours, I could assess the project's performance, scalability, and accuracy under conditions akin to its intended deployment. This comprehensive testing approach helped identify and rectify issues early in the development cycle, ensuring a more robust and reliable final product.