<h2 dir="auto">Automated Testing framework for Takservice.pl website</h2>
<p dir="auto">This is&nbsp;testing framework with using Python, OOP, Selenium, Pytest and Page Object methodology.</p>
<h2>How to run:</h2>
<ol>
<li dir="auto">Copy project files to your local machine.</li>
<li dir="auto">To install all packages from requirements.txt open terminal and use command:&nbsp;<strong>pip install -r requirements.txt</strong></li>
</ol>
<h2 dir="auto"><strong>Project overview:</strong></h2>
<p dir="auto"><strong>--- pages&nbsp;&nbsp;</strong># Folder for implementing page methods and locators.</p>
<p dir="auto"><strong><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</strong>base_page.py&nbsp;&nbsp;</strong># Page methods and assertions, that are available at all endpoints of the project.</p>
<p dir="auto"><strong><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</strong>home_page.py&nbsp;&nbsp;</strong>#&nbsp;Page methods and assertions, that are available at homepage of the project.</p>
<p dir="auto"><strong><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</strong>{other pages}&nbsp;&nbsp;</strong>#&nbsp;Other methods and assertions.</p>
<p dir="auto"><strong>--- tests&nbsp;&nbsp;</strong>#&nbsp;Folder to store test files and conftest.py file.</p>
<p dir="auto"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;conftest.py&nbsp;&nbsp;</strong># Configuration for tests. Implemented browser fixture.</p>
<p dir="auto"><strong><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</strong>test_home_page.py&nbsp;&nbsp;</strong># Test file, contains functions, that reuse methods from pages folder.</p>
<p dir="auto"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{other tests}&nbsp;&nbsp;</strong># Other test files, they contains functions, that reuse methods from pages folder.</p>
<p dir="auto"><strong>requirements.txt&nbsp;&nbsp;</strong># File with requirements for successfull framework run.</p>
<h2 dir="auto">About Page-Object Pattern:</h2>
<p>Page Object is a Design Pattern that is popular in test automation for enhancing test maintenance and reducing code duplication. The tests use the methods of the page object class whenever they need to interact with the UI of that page. The benefit is that if the UI changes for the page, the tests themselves don&rsquo;t need to change, only the code within the page object needs to change. Subsequently, all changes to support that new UI are located in one place.</p>
<h2>About the product:</h2>
<p>&nbsp;</p>