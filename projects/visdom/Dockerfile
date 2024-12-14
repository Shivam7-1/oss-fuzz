FROM gcr.io/oss-fuzz-base/base-builder-python

COPY . $SRC/

# Clone the Visdom repository
RUN git clone --depth 1 https://github.com/fossasia/visdom.git $SRC/visdom

# Install dependencies
RUN python3 -m pip install --no-cache-dir -r $SRC/visdom/test-requirements.txt

COPY build.sh $SRC/

RUN bash $SRC/build.sh

