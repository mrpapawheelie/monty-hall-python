# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="P A P A W H E E L I E Probability Playground",
        page_icon="🎲",
    )

    st.write("# Papa's Probability Playground! 🎲")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        I find visualizing results helps understand concepts like
        probabilty and how the expected result may not be the case
        all of the time. This site focuses on these concepts found 
        in many Machine Learning and Data Science projects.
        **👈 Select a experiment from the sidebar** to see some weird examples.
    """
    )


if __name__ == "__main__":
    run()
