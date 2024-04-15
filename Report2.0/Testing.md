
As mentioned before the nature of the crowd pulse project, 

---


Initially I was using the system on relatively small networks, which did not simulate the environment that the system would be deployed in, i.e. large area networks, that have a much higher device count. So to fix this, I decided to use `Faker`. Faker is a Python module that allows you to quickly generate fake information, such as companies, names, and most importantly for this project, Network information. Using the faker module I was able to create large networks, that would simulate the environment that the crowd pulse system would be deployed in.
##### How was it tested?
Initially the project was tested on small home networks, as that was what I had access to at the time. Due to the nature of the project, testing on small home networks was not the best way to test the project, as it was built for crowd monitoring, on larger scale networks. 

I had to think of a different way to test the project without access to larger scale networks due to the potential data security issues. I landed on Faker, a library for generating synthetic data.

Using the Faker library allowed me to simulate various network environments realistically, This synthetic data generation approach provided a controlled yet expansive testing environment without compromising actual user data. By generating data representative of real-world network behaviours, I could assess the project's performance, scalability, and accuracy under conditions akin to its intended deployment. This comprehensive testing approach helped identify and rectify issues early in the development cycle, ensuring a more robust and reliable final product.

###### What did you test it on
As mentioned earlier the project underwent exhaustive testing across an extensive array of synthetic networks, meticulously crafted utilizing the sophisticated functionalities offered by the Faker library. These simulated environments spanned a broad spectrum of complexity, encompassing everything from modest home-based configurations to expansive networks mirroring the intricate infrastructure typically observed within university campuses or corporate enterprises.
##### How did you get the data
The data acquisition process began with an in-depth analysis of my personal home network, serving as the initial testing ground for the project. Subsequently, the methodology evolved towards the generation of intricate synthetic data sets crafted to accurately emulate real-world scenarios. This sophisticated approach involved meticulously fine-tuning data parameters to ensure a seamless integration Through these iterative steps, a comprehensive data framework was established, enabling exhaustive testing and refinement to drive the project's development forward.