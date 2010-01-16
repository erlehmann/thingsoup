<?xml version="1.0" ?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>thingsoup — ${self.header()}</title>
    </head>

    <body>
        <header>
            <nav>
                <ul>
                    <li>
                        ${h.link_to('Home', url('home'))}
                    </li>
                    <li>
                        ${h.link_to('Index', url('index'))}
                    </li>
                    <li>
                        ${h.link_to('New Thing', url('form_new_thing'))}
                    </li>
                </ul>
            </nav>

            <form>
                <fieldset>
                    <label for="query">Search</label>
                    <input type="search" id="query"/>
                    <input type="submit"/>
                </fieldset>
            </form>
        </header>

        <div class="main">

            <h1>${self.header()}</h1>

            ${next.body()}\

        </div>

        <footer/>
    </body>
</html>
